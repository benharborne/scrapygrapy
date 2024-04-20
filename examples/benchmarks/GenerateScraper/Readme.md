# Local models
The two websites benchmark are:
- Example 1:  https://perinim.github.io/projects
- Example 2: https://www.wired.com (at 17/4/2024)

Both are strored locally as txt file in .txt format  because in this way we do not have to think about the internet connection

The time is measured in seconds

The model runned for this benchmark is Mistral on Ollama with nomic-embed-text

| Hardware           | Example 1 | Example 2 |
| ------------------ | --------- | --------- |
| Macbook 14' m1 pro | 30.54     | 35.76     |
| Macbook m2 max     |           |           |


**Note**: the examples on Docker are not runned on other devices than the Macbook because the performance are to slow (10 times slower than Ollama). Indeed the results are the following:

| Hardware           | Example 1 | Example 2 |
| ------------------ | --------- | --------- |
| Macbook 14' m1 pro |           |           |
# Performance on APIs services
### Example 1: personal portfolio 
**URL**: https://perinim.github.io/projects
**Task**: List me all the projects with their description.

| Name                | Execution time (seconds) | total_tokens | prompt_tokens | completion_tokens | successful_requests | total_cost_USD |
| ------------------- | ------------------------ | ------------ | ------------- | ----------------- | ------------------- | -------------- |
| gpt-3.5-turbo       | 24.215268                | 1892         | 1802          | 90                | 1                   | 0.002883       |
| gpt-4-turbo-preview | 6.614                    | 1936         | 1802          | 134               | 1                   | 0.02204        |

### Example 2: Wired
**URL**: https://www.wired.com
**Task**: List me all the articles with their description.

| Name                | Execution time (seconds) | total_tokens | prompt_tokens | completion_tokens | successful_requests | total_cost_USD |
| ------------------- | ------------------------ | ------------ | ------------- | ----------------- | ------------------- | -------------- |
| gpt-3.5-turbo       |                          |              |               |                   |                     |                |
| gpt-4-turbo-preview |                          |              |               |                   |                     |                |

