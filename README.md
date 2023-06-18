The above code is based on Chorin's operator splitting, which allows us to uncouple the equations so that the incompressibility constaint is not satisfied in each step. Chorin's method results into a predictor corrector approach where we calculate an intermediate velocity ignoring the pressure term, later we use the intermediate velocity and pressure term to get the correct velocity, the later step also satisfies the incompressbility rule.
