class ChaiOrder:
    def __init__(Self, tea_types, sweetness, size):
        Self.tea_types = tea_types
        Self.sweetness = sweetness
        Self.size = size
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["small", "medium", "large"]

print(ChaiUtils.is_valid_size("medium"))
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size": "large"})
order2 = ChaiOrder.from_string("Ginger-Low-Small")
order3 = ChaiOrder("Green", "Low", "Large")
print(order1.tea_types)
