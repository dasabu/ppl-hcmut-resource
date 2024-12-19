class Attribute_Check:
    def __init__(self, name:str, typ:Type, isStatic = False, const = False):pass

class Variable_Check:
    def __init__(self,name,typ,scope, constant=False):pass

class Method_Check:
    def __init__(self, method_name:str, static=False, para:List[VarDecl]=[], rettype=None):pass
    def _enterScope(self):pass
    def _exitScope(self):pass
    def _change_ret_type(self, rettype):pass
	
class Class_Check:
    def __init__(self, name:str, inherited:Class_Check = None):pass
    def add_attribute(self, name:str, att_type:Type, isStatic=False, const=False):pass
    def add_method(self, name:str, isStatic=False, paratype:List[VarDecl]=[], rettype=None):pass
    def get_method(self, method_name:str):pass


class ClassManager:
    def add_class(self, cls_name:str, inherited:str):pass
    def add_method(self, cls_name:str, method_name:str, isStatic=False, paratype:List[Type]=[], rettype = None):pass
    def add_attribute(self, cls_name:str, att_name:str,att_type:Type,isStatic:bool,const:bool):pass
    def get_class(self, class_name:str):pass