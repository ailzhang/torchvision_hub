def get_entrypoints(hub_info):
    hub_info['entrypoints'] = {'wrapper': ['torchvision.models.hub_example', 'https://downget.pytorch.org/models/resnet18-5c106cde.pth']}

def get_required_pkg(hub_info):
    hub_info['required'] = ['torch', 'math']

def get_help_msg(hub_info):
    msg = 'hello world'
    hub_info['help'] = ("/****** Hub Help Section ******/\n"
                        "hello world\n"
                        "/******  End of Message  ******/")

def get_hub_info():
    hub_info = {}
    get_entrypoints(hub_info)
    get_required_pkg(hub_info)
    get_help_msg(hub_info)
    return hub_info


if __name__ == '__main__':
    import pdb
    pdb.set_trace()
    print(get_hub_info())