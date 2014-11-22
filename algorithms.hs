nub' :: (Num a, Eq a) => [a] -> [a]
nub' = foldl (\acc x -> if x `elem` acc then acc else acc ++ [x]) []

