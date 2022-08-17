import importlib
import logging


class Runner:
    PATH_TO_MODULES = "solutions"

    def __init__(self, logger=logging, path_to_modules=PATH_TO_MODULES, **args):
        self.logger = logger
        self.path_to_modules = path_to_modules
        self.args = args

    def get_package_instance(self, module_name):
        module_path = self.path_to_modules + "." + module_name
        self.logger.debug(
            f"CALL get_package_instance() with "
            f"module_name: {module_name!r}, module_path: {module_path!r}"
        )
        return importlib.import_module(self.path_to_modules + "." + module_name)

    def run(self, last_output_data={}):
        self.logger.debug(f"CALL run()")
        splited_runner_plan = self.args["runner_plan"].split(",")
        self.logger.debug(f"splited_runner_plan: {str(splited_runner_plan)}")
        modules_instances = (
            (module_name, self.get_package_instance(module_name))
            for module_name in splited_runner_plan
        )
        self.logger.debug(f"modules_instances: {str(modules_instances)}")

        last_runnable_instance = None
        last_module_name = ""
        for module_name, module_instance in modules_instances:
            self.logger.info(f"Run module_name: {module_name}")
            data_tmp = (
                last_output_data[last_module_name]
                if last_module_name != "" and last_module_name in last_output_data
                else last_output_data
            )
            last_runnable_instance = module_instance.RunnableBlock(
                last_runnable_instance=last_runnable_instance, **self.args
            )
            output_data = last_runnable_instance.run(last_output_data=data_tmp)
            last_output_data.update({module_name: output_data})
            last_module_name = module_name
        return last_output_data, last_module_name
