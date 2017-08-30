import db_connector
import base

""" A collection of functions used to verify certain conditions in database"""

def if_role_in_group(char_id, role):
    role_in_group = False
    char_connector = db_connector.Db_Connector(base.Character)
    for i in char_id:
        char = char_connector.load_from_db('id', i)
        if char[0].family_role.role == role:
            role_in_group = True
            break
    char_connector.close_session()
    return role_in_group
