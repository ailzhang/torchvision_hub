# /**************************For Repo Owner************************************
# entrypoint_list is a tuple of (func_name, module_name, checkpoint_dir).
#     func_name: required, this function should return a model
#     module_name: required, specifies where to load the module in the package
#     checkpoint_url: optional, specifies where to download the checkpoint
# deps_list is a list of dependent package names.
# help_msp is a string, explaining what model each entrypoint points to.
# ****************************************************************************/

entrypoint_list = [
    ('wrapper1',
     'torchvision_hub.models.hub_example',
     'https://download.pytorch.org/models/resnet18-5c106cde.pth'),
    ('wrapper2',
     'torchvision_hub.transforms.hub_example',
     'https://download.pytorch.org/models/resnet18-5c106cde.pth')
    ]
deps_list = ['torch', 'math']
help_msg = ("/****** Hub Help Section ******/\n"
            "hello world\n"
            "/******  End of Message  ******/")


# /****************************************************************************
# ********** Helper functions for Pytorch Hub *********************************
# *************** (Please do not edit) ****************************************
# ****************************************************************************/
KEY_ENTRYPOINTS = 'entrypoints'
KEY_REQUIRED = 'required'
KEY_CHECKPOINT = 'checkpoint'
KEY_MODULE = 'module'
KEY_HELP = 'help'


def add_entrypoint(hub_info, func_name, module_name, checkpoint_url=None):
    hub_info[KEY_ENTRYPOINTS][func_name] = {
            KEY_MODULE: module_name,
            KEY_CHECKPOINT: checkpoint_url}


def set_entrypoints(hub_info, entrypoint_list):
    for func_name, module_name, checkpoint_url in entrypoint_list:
        add_entrypoint(hub_info, func_name, module_name, checkpoint_url)


def set_required(hub_info, deps_list):
    hub_info[KEY_REQUIRED] = deps_list


def set_help(hub_info, help_msg):
    hub_info[KEY_HELP] = help_msg


def get_hub_info():
    hub_info = {KEY_ENTRYPOINTS: {}, KEY_REQUIRED: [], KEY_HELP: ''}
    set_entrypoints(hub_info, entrypoint_list)
    set_required(hub_info, deps_list)
    set_help(hub_info, help_msg)
    return hub_info


if __name__ == '__main__':
    # For local testing
    print(get_hub_info())
