import numpy as np
from scipy.optimize import minimize

# 当前价格
current_prices = np.array([10, 15, 32])

# 不同情景下的收益
good_scenario = np.array([15, 24, 40])
medium_scenario = np.array([11, 18, 30])
bad_scenario = np.array([6, 10, 20])

# 无风险收益率
risk_free_rate = 0.06

# 情景概率（假设每种情景概率相等）
probabilities = np.array([1/3, 1/3, 1/3])

# 计算每种情景下的收益
scenario_returns = np.vstack([good_scenario - current_prices,
                              medium_scenario - current_prices,
                              bad_scenario - current_prices])

# 定义夏普比率的负值（因为我们要最大化夏普比率，而 minimize 是最小化函数）
def negative_sharpe_ratio(weights):
    # 投资组合的预期收益
    portfolio_returns = np.dot(scenario_returns, weights[:-1]) + risk_free_rate * weights[-1]
    expected_return = np.dot(probabilities, portfolio_returns)
    
    # 投资组合的标准差
    portfolio_std = np.sqrt(np.dot(probabilities, (portfolio_returns - expected_return) ** 2))
    
    # 夏普比率
    sharpe_ratio = (expected_return - risk_free_rate) / portfolio_std
    
    # 返回负的夏普比率（因为我们要最大化夏普比率）
    return -sharpe_ratio

# 约束条件：权重之和为 1
constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})

# 初始猜测（均匀分布）
initial_guess = np.ones(4) / 4

# 边界条件：权重必须非负
bounds = [(0, None), (0, None), (0, None), (0, None)]

# 优化
result = minimize(negative_sharpe_ratio, initial_guess, method='SLSQP', constraints=constraints, bounds=bounds)

if result.success:
    optimal_weights = result.x
    print("最佳投资组合权重:", optimal_weights)
    
    # 计算预期收益和标准差
    portfolio_returns = np.dot(scenario_returns, optimal_weights[:-1]) + risk_free_rate * optimal_weights[-1]
    expected_return = np.dot(probabilities, portfolio_returns)
    portfolio_std = np.sqrt(np.dot(probabilities, (portfolio_returns - expected_return) ** 2))
    
    print("预期收益:", expected_return)
    print("投资组合标准差:", portfolio_std)
    print("夏普比率:", (expected_return - risk_free_rate) / portfolio_std)
else:
    print("优化失败")