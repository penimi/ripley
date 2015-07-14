
# /home/disnesquick/Ripley/codegen/yacctab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '7EEB404CD431F4A046DD4A4297CEE143'
    
_lr_action_items = {'TYPEID':([2,4,8,14,17,18,25,30,34,35,36,37,38,39,40,41,42,43,49,],[15,16,20,21,24,-20,-24,38,24,-23,47,-19,-33,-31,38,-10,-32,-30,-9,]),'CLASS':([0,1,6,7,9,10,11,12,16,18,19,25,29,35,37,44,48,],[2,-16,-14,2,-18,-15,-4,-17,-21,-20,-3,-24,-22,-23,-19,-27,-29,]),'RBRACE':([18,25,31,32,33,35,37,38,39,40,41,42,43,45,49,],[-20,-24,44,-28,-6,-23,-19,-33,-31,48,-10,-32,-30,-5,-9,]),'RARROW':([18,25,35,],[28,-24,-23,]),'COMMA':([23,24,26,46,47,],[-8,-26,34,-7,-25,]),'TYPE':([0,1,6,7,9,10,11,12,16,18,19,25,29,35,37,44,48,],[4,-16,-14,4,-18,-15,-4,-17,-21,-20,-3,-24,-22,-23,-19,-27,-29,]),'COLON':([27,],[36,]),'EXCEPTION':([0,1,6,7,9,10,11,12,16,18,19,25,29,35,37,44,48,],[8,-16,-14,8,-18,-15,-4,-17,-21,-20,-3,-24,-22,-23,-19,-27,-29,]),'SERVICE':([0,1,6,7,9,10,11,12,16,18,19,25,29,35,37,44,48,],[14,-16,-14,14,-18,-15,-4,-17,-21,-20,-3,-24,-22,-23,-19,-27,-29,]),'LBRACE':([15,21,],[22,30,]),'LPAREN':([5,20,28,42,],[17,17,17,17,]),'$end':([0,1,3,6,7,9,10,11,12,13,16,18,19,25,29,35,37,44,48,],[-11,-16,-13,-14,-12,-18,-15,-4,-17,0,-21,-20,-3,-24,-22,-23,-19,-27,-29,]),'ID':([0,1,6,7,9,10,11,12,16,17,18,19,22,25,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,48,49,],[5,-16,-14,5,-18,-15,-4,-17,-21,27,-20,-3,5,-24,-22,42,5,-28,-6,27,-23,-19,-33,-31,42,-10,-32,-30,-27,-5,-29,-9,]),'RPAREN':([17,23,24,26,46,47,],[25,-8,-26,35,-7,-25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function_def':([0,7,22,30,31,40,],[1,1,32,39,32,39,]),'empty':([0,],[3,]),'service_def':([0,7,],[6,6,]),'serviced':([30,40,],[41,49,]),'param':([17,34,],[23,46,]),'method':([22,31,],[33,45,]),'type_def':([0,7,],[9,9,]),'serviced_list':([30,],[40,]),'class_def':([0,7,],[10,10,]),'param_list':([17,],[26,]),'method_list':([22,],[31,]),'interface':([0,7,],[11,19,]),'interface_list':([0,],[7,]),'exception_def':([0,7,],[12,12,]),'base':([0,],[13,]),'thing_ref':([30,40,],[43,43,]),'params':([5,20,28,42,],[18,29,37,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> base","S'",1,None,None,None),
  ('params_opt -> empty','params_opt',1,'p_params_opt','parser.py',66),
  ('params_opt -> params','params_opt',1,'p_params_opt','parser.py',67),
  ('interface_list -> interface_list interface','interface_list',2,'p_interface_list','parser.py',83),
  ('interface_list -> interface','interface_list',1,'p_interface_list','parser.py',84),
  ('method_list -> method_list method','method_list',2,'p_method_list','parser.py',83),
  ('method_list -> method','method_list',1,'p_method_list','parser.py',84),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','parser.py',83),
  ('param_list -> param','param_list',1,'p_param_list','parser.py',84),
  ('serviced_list -> serviced_list serviced','serviced_list',2,'p_serviced_list','parser.py',83),
  ('serviced_list -> serviced','serviced_list',1,'p_serviced_list','parser.py',84),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',200),
  ('base -> interface_list','base',1,'p_base','parser.py',204),
  ('base -> empty','base',1,'p_base','parser.py',205),
  ('interface -> service_def','interface',1,'p_interface','parser.py',210),
  ('interface -> class_def','interface',1,'p_interface','parser.py',211),
  ('interface -> function_def','interface',1,'p_interface','parser.py',212),
  ('interface -> exception_def','interface',1,'p_interface','parser.py',213),
  ('interface -> type_def','interface',1,'p_interface','parser.py',214),
  ('function_def -> ID params RARROW params','function_def',4,'p_function_def','parser.py',219),
  ('function_def -> ID params','function_def',2,'p_function_def','parser.py',220),
  ('type_def -> TYPE TYPEID','type_def',2,'p_type_def','parser.py',228),
  ('exception_def -> EXCEPTION TYPEID params','exception_def',3,'p_exception_def','parser.py',233),
  ('params -> LPAREN param_list RPAREN','params',3,'p_params','parser.py',238),
  ('params -> LPAREN RPAREN','params',2,'p_params','parser.py',239),
  ('param -> ID COLON TYPEID','param',3,'p_param','parser.py',247),
  ('param -> TYPEID','param',1,'p_param','parser.py',248),
  ('class_def -> CLASS TYPEID LBRACE method_list RBRACE','class_def',5,'p_class_def','parser.py',256),
  ('method -> function_def','method',1,'p_method','parser.py',261),
  ('service_def -> SERVICE TYPEID LBRACE serviced_list RBRACE','service_def',5,'p_service_def','parser.py',266),
  ('serviced -> thing_ref','serviced',1,'p_serviced','parser.py',271),
  ('serviced -> function_def','serviced',1,'p_serviced','parser.py',272),
  ('thing_ref -> ID','thing_ref',1,'p_thing_ref','parser.py',277),
  ('thing_ref -> TYPEID','thing_ref',1,'p_thing_ref','parser.py',278),
]
