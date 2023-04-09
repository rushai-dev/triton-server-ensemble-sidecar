import tritongrpcclient
import numpy as np
import os

class InferenceService():

    def __init__(self, product) -> None:

        self.product = product

        self.input_name = "INPUT"
        self.output_name = "OUTPUT"
        self.triton_client = tritongrpcclient.InferenceServerClient(url=os.getenv("INFER_URL"), verbose=True)


    def load_image(self, data_bytes: str):
        """
        Loads an encoded image as an array of bytes.
        
        """
        return np.frombytes(data_bytes, dtype=np.uint8)


    def predict(self, inputs):

        res = []

        for input in inputs:

            image_data = self.load_image(input["content-bytes"])
            image_data = np.expand_dims(image_data, axis=0)

            inputs = []
            outputs = []

            inputs.append(tritongrpcclient.InferInput(self.input_name, image_data.shape, "UINT8"))
            outputs.append(tritongrpcclient.InferRequestedOutput(self.output_name))

            inputs[0].set_data_from_numpy(image_data)

            results = self.triton_client.infer(model_name="ensemble",
                                  inputs=inputs,
                                  outputs=outputs)

            output0_data = results.as_numpy(self.output_name)

            results = []

            for values in output0_data:
                results.append(values.decode('UTF-8'))

            res.append(results)
        
        return res