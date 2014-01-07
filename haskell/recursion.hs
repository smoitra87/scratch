maximum' :: (Ord a) => [a] -> a
maximum' [] = error "Empty string"
maximum' [x] = x
maximum' (x:xs) 
        | x > maxTail = x 
        | otherwise = maxTail
        where maxTail = maximum' xs

replicate' :: (Num i, Ord i) => i -> a -> [a]
replicate' n x
        | n <= 0 = []
        | otherwise = x:replicate' (n-1) x

quicksort' :: (Ord a) => [a] -> [a]
quicksort' [] = []
quicksort' (x:xs) = quicksort'(leq x xs) ++ [x] ++ quicksort' (gt x xs)
                where leq x xs = [y | y<-xs , y <= x]
                      gt x xs = [y | y<-xs , y > x]
       

