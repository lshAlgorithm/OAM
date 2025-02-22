# Optimal Arbitrage Mix

> [!important]
> 
> JUST A TOY! For the paper of my general education class.
> 
> This repository does **NOT** constitute any investement advice.

1. buy in/out
	- no bounds
	- output:
	```bash
	最佳投资组合权重: [-15182.08331436   7591.04167528   1518.20831382   6073.83332525]
	预期收益: 4919.055071291425
	投资组合标准差: 4.123916874067521e-05
	夏普比率: 119279685.34534737
	```

2. buy in only:
	- with boudns
	- output:
	```bash
	最佳投资组合权重: [4.94049246e-15 7.72681675e-01 6.66272593e-14 2.27318325e-01]
	预期收益: 1.8165630076177486
	投资组合标准差: 4.431239396945929
	夏普比率: 0.3964044481163432
	```

3. Scale up the share options by adding:
   1. current_prices
   2. bounds
   3. initial_guess