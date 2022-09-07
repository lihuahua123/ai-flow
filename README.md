# AIFlow

[![CI](https://github.com/flink-extended/ai-flow/actions/workflows/flink_ai_flow_ci.yml/badge.svg)](https://github.com/flink-extended/ai-flow/actions/workflows/flink_ai_flow_ci.yml)
[![codecov](https://codecov.io/gh/flink-extended/ai-flow/branch/master/graph/badge.svg?token=ISWZNXUYO5)](https://codecov.io/gh/flink-extended/ai-flow)

## Introduction

AIFlow is an event-driven workflow management framework that allows users to write machine learning pipelines that contain both stream and batch jobs.

Such capability is quite useful for complicated real-time machine learning systems as well as other real-time workflows.

Learn more about AIFlow at https://ai-flow.readthedocs.io

## Features

1. Event-driven: AIFlow schedule workflow and jobs based on events. This is more efficient than status-driven scheduling and be able to schedule the workflows that contain stream jobs.

2. Extensible: Users can easily define their own operators and executors to submit various types of tasks to different platforms.

3. Exactly-once: AIFlow provides an event processing mechanism with exactly-once semantics, which means that your tasks will never be missed or repeated even if a failover occurs.

## Contributing

We happily welcome contributions to AIFlow in any ways, whether reporting problems, drafting features, or contributing code changes.
You can report problems to request features in the [GitHub Issues](https://github.com/flink-extended/ai-flow/issues).
If you want to contribute code changes, please check out the [contributing documentation](./CONTRIBUTING.md).


## Contact Us

For more information, we recommend you to join the **AIFlow Community Group** on the [Google Groups](https://groups.google.com) to contact us: **aiflow@googlegroups.com**.

You can also join the group on the [DingTalk](https://www.dingtalk.com). The number of the DingTalk group is `35876083`, which group can also be joined by scanning the QR code below:

![](https://raw.githubusercontent.com/wiki/alibaba/flink-ai-extended/images/dingtalk_qr_code.png)
