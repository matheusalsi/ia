# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# A iteração de valor calcula estimativas de k passos dos valores ótimos, Vk. Além
# de executar a iteração de valor, implemente os seguintes métodos
# para ValueIterationAgent usando Vk.
# • computeActionFromValues(state) calcula a melhor ação de acordo com a
# função de valor fornecida por self.values.
# • computeQValueFromValues(state, action) retorna o valor-Q do par (estado,
# ação) dado pela função de valor em self.values. Lembre-se que, uma vez
# que o valor de cada estado está determinado, e conhecendo as
# probabilidades de transição (obtidas com getTransitionStatesAndProbs),
# podemos calcular os valores Q de pares estado-ação.


import mdp, util
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        # Write value iteration code here
                
        for iteration in range(iterations):
            counter = util.Counter()
            states = self.mdp.getStates()

            for state in states:
                bestReward = float('-inf')
                possibleActions = self.mdp.getPossibleActions(state)

                for action in possibleActions:
                    currentReward = self.getQValue(state, action)
                    bestReward = max(bestReward, currentReward)
                    counter[state] = bestReward
                    
            self.values = counter


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        listOfTransitionStates = self.mdp.getTransitionStatesAndProbs(state, action)
        qValue = 0

        for nextState, probability in listOfTransitionStates:
            currentReward = self.mdp.getReward(state, action, nextState)
            qValue += (probability * (currentReward + self.discount * self.getValue(nextState)))
        
        return qValue

        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        isTerminal = self.mdp.isTerminal(state)

        if not(isTerminal):
            maxValue = float('-inf')
            possibleActions = self.mdp.getPossibleActions(state)
            for action in possibleActions:
                qValue = self.getQValue(state, action)
                if qValue > maxValue:
                    bestAction = action
                    maxValue = qValue
            return bestAction
        else:
            return None
        
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
    



   