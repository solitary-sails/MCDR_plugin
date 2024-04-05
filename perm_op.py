from mcdreforged.api.types import *

PLUGIN_METADATA = {
    'id' :'perm_op',
    'version' : '0.0.1',
    'name' : 'permissionOP',
    'description' : 'Grant OP permissions to users with appropriate MCDR permissions',
    'author' : 'sails',
   
}

config = {
'requiredPem': 3
}
default_config = config.copy()


def on_load(server,prev):
    global config
    config = server.load_config_simple('perm_op.json', default_config)
    server.save_config_simple(config,'perm_op.json')



def on_user_info(server: PluginServerInterface, info: Info):
    if info.content == '!!op':
        if server.get_permission_level(info.player) >= config['requiredPem']:
            server.execute('/op {}'.format(info.player))
        else:
            server.tell(player=info.player,text='Insufficient permission')