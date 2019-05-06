from Robot import Robot
from Obstacle import Obstacle
from Goal import Goal
import matplotlib.pyplot as plt

def main():
    """
    This is the function for instantiating object of Robot, Goal, and Obstacles.
    This programs runs until distance of robot is less then 0.9 to goal and 
    during this process it keeps on deciding next move and then exectuing it.
    """

    obstacle1 = Obstacle(pos_x=11.0, pos_y=5.0, alpha=1.0, mu=4.0)
    obstacle2 = Obstacle(pos_x=12.0, pos_y=8.0, alpha=1.0, mu=4.0)
    obstacle3 = Obstacle(pos_x=10.0, pos_y=10.0, alpha=1.0, mu=4.0)
    obstacles = [obstacle1, obstacle2, obstacle3]
    goal = Goal(pos_x=18.0, pos_y=18.0, alpha=1.0, mu=4.0)
    my_robot = Robot(pos_x=5.0, pos_y=5.0, sensor_range=2.0, npts=60)

    plt.figure()
    plt.axis([0, 20, 0, 20])
    
    while my_robot.get_distance_to_goal(goal=goal) > 0.9:

        plt.plot(my_robot.get_coordinate("x"), my_robot.get_coordinate("y"),"o")
        plt.plot(obstacle1.get_coordinate("x"), obstacle1.get_coordinate("y"),"o")
        plt.plot(obstacle2.get_coordinate("x"), obstacle2.get_coordinate("y"),"o")
        plt.plot(obstacle3.get_coordinate("x"), obstacle3.get_coordinate("y"),"o")
        plt.plot(goal.get_coordinate("x"), goal.get_coordinate("y"),"o")

        my_robot.decide_next_move(goal=goal, obstacles=obstacles)
        my_robot.take_next_move()
        plt.draw()
        plt.pause(0.05)

if __name__ == "__main__":

    main()    