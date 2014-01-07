head' :: [a] -> a
head' [] = error "Empty list"
head' (x:_) = x

calcBMI :: (RealFloat a) => [(a,a)] -> [a]
calcBMI xs = [ bmi w h | (w,h) <- xs]
    where bmi w h = w / h^2

cylinder :: Float -> Float -> Float
cylinder r h = 
        let toparea = pi * r ^ 2 
            sidearea = 2 * pi * r * h
        in 2*toparea + sidearea

calcBMIlet :: (RealFloat a) => [(a,a)] -> [a]
calcBMIlet xs = [ bmi | (w,h)<-xs, let bmi = w/h^2]

calcBMIletfunc :: (RealFloat a) => [(a,a)] -> [a]
calcBMIletfunc xs = [ bmi w h | (w,h)<-xs, let bmi w h = w/h^2]

            

