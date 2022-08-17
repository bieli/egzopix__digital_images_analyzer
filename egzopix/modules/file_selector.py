from typing import Union, Tuple, Dict, List

from egzopix.modules import VisualModule, VisualModuleProperty


class FileSelectorVisualModule(VisualModule):
    inputs: Dict[str, VisualModuleProperty] = {
        "file_path": VisualModuleProperty("file_name", "File name", str, True),
    }
    outputs: Dict[str, VisualModuleProperty] = {
        "file_name": VisualModuleProperty("file_name", "File name", str, True),
        "file_temp": VisualModuleProperty(
            "file_temp", "File temporary path", str, True
        ),
        "file_body": VisualModuleProperty("file_body", "File body", bytes, False),
    }
    exceptions: Dict[str, List[Union[str, None]]] = {"inputs": [], "outputs": []}

    def process(
        self, input: VisualModuleProperty
    ) -> Tuple[Union[None, dict], Union[None, dict]]:
        # TODO: add catching exceptions and fill self.exceptions field
        # TODO: add file_temp to outputs
        self.inputs["file_path"] = input
        path_to_file = self.inputs["file_path"].payload
        if not isinstance(path_to_file, str):
            self.exceptions["input"].append(
                'Wrong type in "input_path" - expected "str" type!'
            )
            return self.outputs, self.exceptions

        with open(str(self.inputs["file_path"].payload), "rb") as file_h:
            self.outputs["file_name"] = self.inputs["file_path"]
            self.outputs["file_body"] = VisualModuleProperty(
                "file_body", "File body", bytes, False, file_h.read()
            )
        return self.outputs, None

    def __str__(self) -> str:
        return str(self.dict())
