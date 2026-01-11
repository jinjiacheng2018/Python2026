# Allure查看报告说明

# 一、Allure 必须分清的两样东西（99% 新手卡这）

| 名称                | 作用               | 安装方式                        |
| ----------------- | ---------------- | --------------------------- |
| **allure-pytest** | pytest → 生成 json | `pip install allure-pytest` |
| **Allure CLI**    | json → HTML 报告   | **单独安装**（不是 pip）            |

👉 你现在 **已经有前者，缺后者**

---

# 二、Windows 安装 Allure CLI（最稳妥做法）✅

## ✅ 方法一：官方 ZIP 安装（最推荐，企业常用）

### 1️⃣ 下载 Allure

打开浏览器，下载 **Allure Commandline（zip）**，例如：https://github.com/allure-framework/allure2/releases/tag/2.30.0

👉 搜索关键词：

> **Allure Commandline GitHub Release**

下载类似：

```text
allure-2.27.0.zip   （版本号可能不同）
```

---

### 2️⃣ 解压到固定目录（重要）

例如：

```text
D:\tools\allure-2.27.0\
```

目录结构应是：

```text
D:\tools\allure-2.27.0\
├─ bin\
│  ├─ allure.bat   ✅
│  └─ allure
├─ lib\
└─ plugins\
```

---

### 3️⃣ 配置环境变量（关键一步）

#### 添加到 **Path**

```text
D:\tools\allure-2.27.0\bin
```

步骤（简述）：

* 系统设置 → 环境变量
* Path → 新增
* 粘贴上面路径
* 确定 → **重开 CMD / PowerShell**

---

### 4️⃣ 验证是否成功

重新打开命令行：

```bash
allure --version
```

如果看到版本号：

```text
2.27.0
```

🎉 **安装成功**

---

# 三、重点：真正“看报告” 🎉
```bash
# 进入到报告的目录下
cd /d/MyWorkspaces/Python2026/report

# 生成报告
allure generate allure-results -o allure-html --clean

# 查看报告(浏览器会自动打开 Allure 报告)
allure open allure-html
```

---

# 四、如果你想“最快验证”（不想生成目录）

```bash
allure serve report/allure-results
```

👉 临时服务，验证用，很快看到页面。

---

# 五、常见问题排雷（你可能马上会遇到）

### ❓ 双击 `index.html` 打不开？

✔ 正常，Allure 需要本地服务

---

### ❓ 中文会不会乱码？

✔ 一般不会
✔ Allure 内部用 UTF-8
⚠️ 需要 JDK（通常你机器已经有）

---

### ❓ 需要 Java 吗？

✔ **需要 JDK 8+**
可验证：

```bash
java -version
```

---

# 六、一步到位（给你企业级做法）

以后你可以只记住一句：

```text
pytest  →  allure-results  →  allure-report
```

并把下面流程固化：

```bash
python run.py
allure generate report/allure-results -o report/allure-report --clean
allure open report/allure-report
```

---

# 七、你现在所处的阶段（说句实在的）

你已经完整走通了：

✅ pytest
✅ 参数化
✅ 日志
✅ Allure JSON
⬜ **Allure CLI（最后一步）**

**这已经是“中高级测试工程师”的完整链路了。**

---

如果你愿意，下一步我可以帮你 **直接把 Allure CLI 调用也写进 `run.py`**，做到：

```bash
python run.py
# 自动生成 + 打开报告
```

这在公司里是非常加分的。
