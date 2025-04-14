/*
 * Created on May 12, 2005
 *
 */
package it.unibo.ai.search.mc;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.List;
import java.util.Properties;

//import aima.core.search.framework.*;
//import aima.core.search.uninformed.*;
//import aima.core.search.informed.*;

import aima.core.agent.Action;

import aima.core.search.framework.SearchAgent;
import aima.core.search.framework.evalfunc.HeuristicFunction;
import aima.core.search.framework.problem.GoalTest;
import aima.core.search.framework.problem.Problem;
import aima.core.search.framework.problem.StepCostFunction;
import aima.core.search.framework.qsearch.GraphSearch;
import aima.core.search.framework.qsearch.TreeSearch;
import aima.core.search.uninformed.BreadthFirstSearch;
import aima.core.search.uninformed.DepthFirstSearch;
import aima.core.search.uninformed.DepthLimitedSearch;
import aima.core.search.informed.AStarSearch;
import aima.core.search.informed.GreedyBestFirstSearch;
import aima.core.search.local.HillClimbingSearch;

/**
 * @author fchesani
 *
 */
public class MissionariCannibaliDemo {
 
	
	public static void main(String[] args) {
		/*
		 * MCState implementa tutte queste interfacce:
		 * 	- GoalTest,
		 * 	- StepCostFunction,
		 *	- HeuristicFunction
		 */
		MCState initState = new MCState();

		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
			/**
			 * Constructs a problem with the specified components, which includes a step
			 * cost function.
			 * 
			 * @param initialState:
			 *            the initial state of the agent.
			 * @param actionsFunction:
			 *            a description of the possible actions available to the agent.
			 * @param resultFunction:
			 *            a description of what each action does; the formal name for
			 *            this is the transition model, specified by a function
			 *            RESULT(s, a) that returns the state that results from doing
			 *            action a in state s.
			 * @param goalTest:
			 *            test determines whether a given state is a goal state.
			 * @param stepCostFunction:
			 *            a path cost function that assigns a numeric cost to each path.
			 *            The problem-solving-agent chooses a cost function that
			 *            reflects its own performance measure.
			 */
			Problem problem = new Problem(initState,
					new MCActionsFunction(),
					new MCResultFunction(),
					initState,
					initState);
			
			SearchAgent agent;
			
			{
				System.out.println("\nPress enter to execute Breadth First Search (Tree Search)...");
				br.readLine();
				System.out.println("\nBreadth First (Tree Search):");
				BreadthFirstSearch search = new BreadthFirstSearch(new TreeSearch());
				agent = new SearchAgent(problem, search);
				printActions(agent.getActions());
				printInstrumentation(agent.getInstrumentation());
			}
			
			{
				System.out.println("\nPress enter to execute Breadth First Search (Graph Search)...");
				br.readLine();
				System.out.println("\nBreadth First (Graph Search):");
				BreadthFirstSearch search = new BreadthFirstSearch(new GraphSearch());
				agent = new SearchAgent(problem, search);
				printActions(agent.getActions());
				printInstrumentation(agent.getInstrumentation());
			}
			
			{
				System.out.println("\nPress enter to execute Depth First Search (Graph Search)...");
				br.readLine();
				System.out.println("\nDepth First (Graph Search):");
				DepthFirstSearch search = new DepthFirstSearch(new GraphSearch());
				agent = new SearchAgent(problem, search);
				printActions(agent.getActions());
				printInstrumentation(agent.getInstrumentation());
			}
			
//			{
//				System.out.println("\nPress enter to execute Depth First (without repetition checks):");
//				br.readLine();
//				System.out.println("\nDepth First (without repetition checks):");
//				DepthFirstSearch search = new DepthFirstSearch(new TreeSearch());
//				agent = new SearchAgent(problem, search);
//				printActions(agent.getActions());
//				printInstrumentation(agent.getInstrumentation());
//			}
			
			{
				System.out.println("\nPress enter to execute Depth Limited Search...");
				br.readLine();
				System.out.println("\nDepth Limited:");
				DepthLimitedSearch search = new DepthLimitedSearch(11);
				agent = new SearchAgent(problem, search);
				printActions(agent.getActions());
				printInstrumentation(agent.getInstrumentation());
			}
			
			
			{
				System.out.println("\nPress enter to execute Greedy Best First Search (Tree Search)...");
				br.readLine();
				System.out.println("\nGreedy (Tree Search):");
				GreedyBestFirstSearch search = new GreedyBestFirstSearch(new TreeSearch(),initState);
				agent = new SearchAgent(problem, search);
				printActions(agent.getActions());
				printInstrumentation(agent.getInstrumentation());
			}
			
			{
				System.out.println("\nPress enter to execute Hill Climbing Search...");
				br.readLine();
				System.out.println("\nHill Climbing:");
				HillClimbingSearch search = new HillClimbingSearch(initState);
				agent = new SearchAgent(problem, search);
				printActions(agent.getActions());
				printInstrumentation(agent.getInstrumentation());
			}
			
			{
				System.out.println("\nPress enter to execute A* Search (Tree Search)...");
				br.readLine();
				System.out.println("\nAStar (Tree Search):");
				AStarSearch search = new AStarSearch(new TreeSearch(), initState);
				agent = new SearchAgent(problem, search);
				printActions(agent.getActions());
				printInstrumentation(agent.getInstrumentation());
			}
			
			{
				System.out.println("\nPress enter to execute A* Search (Graph Search)...");
				br.readLine();
				System.out.println("\nAStar (Graph Search):");
				AStarSearch search = new AStarSearch(new GraphSearch(), initState);
				agent = new SearchAgent(problem, search);
				printActions(agent.getActions());
				printInstrumentation(agent.getInstrumentation());
			}
			
			
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	private static void printInstrumentation(Properties properties) {
		Iterator<Object> keys = properties.keySet().iterator();
		while (keys.hasNext()) {
			String key = (String) keys.next();
			String property = properties.getProperty(key);
			System.out.println(key + " : " + property.toString());
		}

	}

	private static void printActions(List<Action> actions) {
		for (int i = 0; i < actions.size(); i++) {
			String action = actions.get(i).toString();
			System.out.println(action);
		}
	}
}
