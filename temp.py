from cfg import ContextFreeGrammar
from typeDef import TypeDefinition
import parser


typedef = TypeDefinition.from_filename("simpleCalc/typedef")
cfg = ContextFreeGrammar.load(typedef, "simpleCalc/CFG4")
action, goto = parser.genActionGoto(typedef, cfg)
action.save("simpleCalc/calc_action")
goto.save("simpleCalc/calc_goto")
exit()
