def square(x):
    """ square numpy array
    
    Args:
    
        x (ndarray): input array
        
    Returns:
    
        y (ndarray): output array
    
    """
    
    y = x**2
    return y
    
#con_opt = new_budget_constraint(result.x) - slettes
#u_opt = utility(con_opt,v,l_opt,epsilon) - slettes
#bounds = ((0,1) , (0,1) , (0,1) , (0.5,1.5) , (0,1)) - slettes

###total_tax_revenue_updated = np.sum(tau_0 * wage_range * labour_range_updated + tau_1*np.max - slettes(wage_range*labour_range_updated-k,0)) - slettes
####print(f'The total tax rate is =  {total_tax_revenue_updated:.2f}') - slettes