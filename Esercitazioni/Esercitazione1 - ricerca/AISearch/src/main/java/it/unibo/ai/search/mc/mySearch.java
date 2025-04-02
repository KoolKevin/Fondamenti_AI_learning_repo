package it.unibo.ai.search.mc;

import aima.core.search.framework.SearchAgent;
import aima.core.search.framework.problem.Problem;

public class mySearch {

	public static void main(String[] args) {
		MCState initState = new MCState();
		/*
		 * aima.core.search.framework.problem.Problem.Problem(
			Object initialState,
			ActionsFunction actionsFunction,
			ResultFunction resultFunction,
			GoalTest goalTest,
			StepCostFunction stepCostFunction
		   )
		 */
		Problem problem = new Problem(initState,
				new MCActionsFunction(),
				new MCResultFunction(),
				initState,
				initState);
		
		SearchAgent agent;
		// ...
	}

}
