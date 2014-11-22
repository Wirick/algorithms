/* Module for a general graph search problem. */
module.exports = function (startState, endState, 
						   goalTest, successorFn,
						   incidents) {
	return {
		getStartState: function () {
			return startState;
		},
		getEndState: function() {
			return endState;
		},
		getSuccessors: function(node) {
			return successorFn(node, incidents);
		},
		goalTest: function(node) {
			return goalTest(node, endState);
		}
	};
};
