def validate_equation(n):
    sum_result=0
    excepted_result=2**(n+1)-1

    for i in range(n+1):
        sum_result +=2**i

    if sum_result == excepted_result:
        print(f"the equatins hold true for n ={n}.")
    else:
        print(f"the equations does not hold true for n={n}.")        


validate_equation(0)        
validate_equation(1)  
validate_equation(2)  
validate_equation(3)  
validate_equation(4)  