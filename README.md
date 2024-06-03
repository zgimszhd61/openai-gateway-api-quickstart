# 多功能高效OpenAI网关解决方案
### 价值主张

**程序功能**:  
- 实现一个OpenAI网关

**优势**:
1. **多OpenAI-SK轮训**: 支持多种OpenAI-SK进行轮询，确保高效利用资源。
2. **不同模型无感切换**: 无缝切换不同的AI模型，提升用户体验。
3. **缓存省钱**: 利用缓存机制减少重复请求，节省使用成本。
4. **定制执行流程**: 提供定制化的执行流程，满足不同需求。
5. **切面安全**: 采用切面编程确保安全性。
6. **无感切换**: 实现无感知的模型切换，提高系统的稳定性和响应速度。
7. 密钥无感轮换.

**总结**: 
该程序为用户提供了一个强大的OpenAI网关，支持多种功能，确保高效、安全和经济地利用OpenAI资源。

### 用法
#### 第一步：
 - 将你想要实现的业务功能（譬如打日志、后置safeguard等）添加到main.py

### 第二步： 
 - 业务要使用的时候，只需要定义OpenAI时，添加如下语句
```
client = OpenAI(
            base_url="http://127.0.0.1:8000",
            api_key="abcaaa-",
)
```

### 如何拓展其他接口
 - 参考官方文档规范，先跑通mock数据：https://platform.openai.com/docs/api-reference/chat/create
