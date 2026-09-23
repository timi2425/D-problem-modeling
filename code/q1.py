# ============================================================
# 15. 计算45个最大安全载荷
# ============================================================

results = []

for service_id in services["服务区编号"]:

    row = {
        "服务区": service_id
    }

    for model in ["A", "B", "C"]:

        qmax = max_safe_payload(
            model,
            service_id,
            reserve_ratio=0.20
        )

        row[f"{model}型最大安全载荷"] = qmax

    results.append(row)


payload_table = pd.DataFrame(
    results
)


print("\n==============================")
print("最大安全载荷结果")
print("==============================")

print(payload_table)
