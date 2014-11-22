/* Module for search algorithms. */

/* Given a SEARCHPROBLEM in 
 * standard form, performs a depth first search to enumerate the set
 * of paths. I picked DFS because there is a finite search space and 
 * no cycles, and I like stacks. Every time a path is found between
 * a start and end state, the function calls back with the path. */
exports.dfsPath = function (searchProblem, callback) {
	var startNode = [searchProblem.getStartState(),[]],
		stack = [],
		end = searchProblem.getEndState,
		succ = searchProblem.getSuccessors,
		goal = searchProblem.goalTest;
		paths = []
	stack.push(startNode);
	while (true) {
		if (stack.length > 0) {
			var current = stack.pop();
			if (goal(current)) {
				callback(null, current[1].concat(current[0]));
			} else {
				var newNodes = succ(current);
				for (var i = 0; i < newNodes.length; i += 1) {
					stack.push(newNodes[i]);
				}
			}
		} else if (stack.length == 0) {
			break;
		}
	}
};

/* Standard binary search function takes a sorted DICtionary and
 * a WORD and returns the index of the WORD in the DIC, and -1
 * if no such index exists. */
exports.binarySearch = function(word, dic) {
    var len = dic.length,
        halfway = Math.floor(len/2),
        startIndex = 0,
        endIndex = len-1,
        end = false;
    while ((endIndex > startIndex) && !end) {
        if (endIndex - startIndex == 1) {
            end = true;
        }
        if (dic[halfway] < word) {
            startIndex = halfway;
            halfway += Math.ceil((endIndex - startIndex)/2);
        } else if (dic[halfway] > word) {
            endIndex = halfway;
            halfway -= Math.ceil((endIndex - startIndex)/2);
        } else {
            return Math.floor(halfway);
        }
    }
    return -1;
}
