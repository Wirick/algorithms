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

/* Given an integer N, returns the set of incident verticies for the boggle
 * problem of size N, in the form of 'x1, y2': [[x2, y2], [x3, y3], ...]
 * corresponding to the adjacent squares of each vertex. Eg. [0, 0]
 * has incidents [0, 1] and [1, 0] and [1, 1]. */
exports.incidents = function(n) {
    var dents = {};
	for (var i = 0; i < n; i += 1) {
		for (var j = 0; j < n; j += 1) {
			var place = i.toString() + ':' + j.toString();
			dents[place] = [];
		} 
	}
    for (var i = 0; i < n; i += 1) {
        for (var j = 0; j <= n-1; j += 1) {
			var place = i.toString() + ':' + j.toString();
            if (i == 0) {
                if (j == 0) {
                  dents[place].push(i.toString() + ':' + (j+1).toString());
                  dents[place].push((i+1).toString() + ':' + j.toString());
				  dents[place].push((i+1).toString() + ':' + (j+1).toString());
                } else if (j == n-1) {
                  dents[place].push(i.toString() + ':' + (j-1).toString());
                  dents[place].push((i+1).toString() + ':' + j.toString());
				  dents[place].push((i+1).toString() + ':' + (j-1).toString());
                } else {
                  dents[place].push(i.toString() + ':' + (j+1).toString());
                  dents[place].push(i.toString() + ':' + (j-1).toString());
                  dents[place].push((i+1).toString() + ':' + j.toString());
				  dents[place].push((i+1).toString() + ':' + (j+1).toString());
				  dents[place].push((i+1).toString() + ':' + (j-1).toString());
                }
            } else if (i == n-1) {
                if (j == 0) {
                  dents[place].push(i.toString() + ':' + (j+1).toString());
                  dents[place].push((i-1).toString() + ':' + j.toString());
				  dents[place].push((i-1).toString() + ':' + (j+1).toString());
				  } else if (j == n-1) {
                  dents[place].push(i.toString() + ':' + (j-1).toString());
                  dents[place].push((i-1).toString() + ':' + j.toString());
				  dents[place].push((i-1).toString() + ':' + (j-1).toString());
                } else {
                  dents[place].push(i.toString() + ':' + (j+1).toString());
                  dents[place].push(i.toString() + ':' + (j-1).toString());
                  dents[place].push((i-1).toString() + ':' + j.toString());
				  dents[place].push((i-1).toString() + ':' + (j-1).toString());
				  dents[place].push((i-1).toString() + ':' + (j+1).toString());
                }
            } else if (j == 0) {
                dents[place].push(i.toString() + ':' + (j+1).toString());
                dents[place].push((i+1).toString() + ':' + j.toString());
                dents[place].push((i-1).toString() + ':' + j.toString());
				dents[place].push((i+1).toString() + ':' + (j+1).toString());
				dents[place].push((i-1).toString() + ':' + (j+1).toString());
            } else if (j == n-1) {
                dents[place].push(i.toString() + ':' + (j-1).toString());
                dents[place].push((i-1).toString() + ':' + j.toString());
                dents[place].push((i+1).toString() + ':' + j.toString());
				dents[place].push((i+1).toString() + ':' + (j-1).toString());
				dents[place].push((i-1).toString() + ':' + (j-1).toString());
            } else {
                  dents[place].push(i.toString() + ':' + (j+1).toString());
                  dents[place].push(i.toString() + ':' + (j-1).toString());
                  dents[place].push((i-1).toString() + ':' + j.toString());
                  dents[place].push((i+1).toString() + ':' + j.toString());
				  dents[place].push((i+1).toString() + ':' + (j+1).toString());
				  dents[place].push((i+1).toString() + ':' + (j-1).toString());
				  dents[place].push((i-1).toString() + ':' + (j-1).toString());
				  dents[place].push((i-1).toString() + ':' + (j+1).toString())
            }
        }
    }
	return dents;
}
