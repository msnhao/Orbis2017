from PythonClientAPI.Game import PointUtils
from PythonClientAPI.Game.Entities import FriendlyUnit, EnemyUnit, Tile
from PythonClientAPI.Game.Enums import Direction, MoveType, MoveResult
from PythonClientAPI.Game.World import World

class PlayerAI:

    def __init__(self):
        
        squadDir = 0;	#0: North,	1:West,	2:South,	3: East
	    squadLeader = 0;	#ID of squad leader
	    squadPos = 0;		#0: Leader, -1: Left Wing,	1: Right Wing	
	    squadCount = 1;	#Number of people in squad

        """
        Any instantiation code goes here
        """
        pass

    def do_move(self, world, friendly_units, enemy_units):
        """
        This method will get called every turn.
        
        :param world: World object reflecting current game state
        :param friendly_units: list of FriendlyUnit objects
        :param enemy_units: list of EnemyUnit objects
        """
        # Fly away to freedom, daring fireflies
        # Build thou nests
        # Grow, become stronger
        # Take over the world
        for unit in friendly_units:
            path = world.get_shortest_path(unit.position,
                                           world.get_closest_capturable_tile_from(unit.position, None).position,
                                           None)
            if path: world.move(unit, path[0])
