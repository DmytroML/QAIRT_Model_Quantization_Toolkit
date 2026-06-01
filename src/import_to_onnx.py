from ultralytics import YOLO
import onnx
import onnxruntime as ort


class get_onnx_models():
    def __init__(self, model_name, imgsz):
        self.model_name = model_name
        self.imgsz = imgsz

    def import_model(self):
        # Load a COCO-pretrained YOLO11n model
        model = YOLO(f"./models/{self.model_name}.pt")
        # Export the model
        model.export(format="onnx", optimize=True, simplify=True, imgsz=self.imgsz, dynamic=False)
        print(f"Модель {self.model_name} експортована в ONNX формат!")

    def modify_onnx(self):
        # Load the ONNX model
        model_onnx = onnx.load(f"./models/{self.model_name}.onnx")

        graph = model_onnx.graph
        # Знайти всі Concat ноди
        for node in graph.node:
            if node.op_type == "Concat":
                for out in node.output:
                    if out == "output0":  # або як називається фінальний вихід
                        final_concat = node
                        concat_inputs = list(node.input)
                        print(f"Знайдено: {concat_inputs}")

        # Отримати shape інформацію для нових виходів
        shape_info = {vi.name: vi for vi in graph.value_info}
        shape_info.update({o.name: o for o in graph.output})

        new_outputs = []
        output_names = ["boxes", "scores"]  # нові імена

        # Замінити один вихід на два окремих
        for i, inp_name in enumerate(concat_inputs):
            # Знайти shape тензора
            if inp_name in shape_info:
                vi = shape_info[inp_name]
            else:
                # Створити базовий ValueInfo якщо немає
                vi = onnx.helper.make_tensor_value_info(inp_name, onnx.TensorProto.FLOAT, None)

            # Перейменувати для зручності
            new_vi = onnx.helper.make_tensor_value_info(
                output_names[i],
                onnx.TensorProto.FLOAT,
                None
            )
            new_outputs.append(new_vi)

            # Перенаправити вихід — знайти ноду що продукує цей тензор
            # і додати alias якщо потрібно
            for node in graph.node:
                for j, out in enumerate(node.output):
                    if out == inp_name:
                        node.output[j] = output_names[i]
                        print(f"  Перенаправлено: {inp_name} → {output_names[i]}")

        # Видалити фінальний Concat з графу
        graph.node.remove(final_concat)

        # Замінити виходи моделі
        while len(graph.output) > 0:
            graph.output.pop()

        graph.output.extend(new_outputs)

        # Зберегти
        onnx.save(model_onnx, f"./models/{self.model_name}_split.onnx")
        print("Збережено split модель!")    
        
    def check_results(self):
        '''Перевірка результатів'''
        # Load the session
        session = ort.InferenceSession(f"./models/{self.model_name}_split.onnx")
        # Get output details
        outputs = session.get_outputs()
        for output in outputs:
            print(f"Name: {output.name}")
            print(f"Shape: {output.shape}")
            print(f"Type: {output.type}")

#get = get_onnx_models('yolo11s', 640)
#get.export_model()
#get.modify_onnx()
#get.check_results()
