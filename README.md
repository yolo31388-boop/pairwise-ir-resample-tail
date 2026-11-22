# pairwise-ir-resample-tail

## 领域

游戏、图形与多媒体

## 主题

混响 IR 重采样

## 说明

IR 重采样、尾音长度重算与单次归一化。

初始状态下 `media/ir_resample_tail.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
