# lightgbm上线

这里是lightgbm如何在线上读取模型的例子。
下面是读取的lightgbm的模型格式（json格式）
{
    "max_feature_idx": 67, 
    "num_class": 1, 
    "name": "tree", 
    "version": "v2", 
    "feature_names": [
        "feature_0", 
        ...........
    ], 
    "label_index": 0, 
    "num_tree_per_iteration": 1, 
    "tree_info": [
        {
            "num_leaves": 31, 
            "num_cat": 0, 
            "tree_index": 0, 
            "tree_structure": {
                "internal_count": 13600, 
                "right_child": {
                    "internal_count": 1573, 
                    "right_child": {
                        "internal_count": 216, 
                        "right_child": {
                            "internal_count": 167, 
                            "right_child": {
                                "internal_count": 137, 
                                "right_child": {
                                    "internal_count": 87, 
                                    "right_child": {
                                        "leaf_index": 30, 
                                        "leaf_value": -2.0851412300725425, 
                                        "leaf_count": 62
                                    }, 
                                    "split_feature": 59, 
                                    "missing_type": "None", 
                                    "default_left": true, 
                                    "internal_value": 1.0279, 
                                    "threshold": 0.055595500000000006, 
                                    "split_gain": 14.675999641418457, 
                                    "split_index": 29, 
                                    "decision_type": "<=", 
                                    "left_child": {
                                        "leaf_index": 26, 
                                        "leaf_value": -2.2353545338918526, 
                                        "leaf_count": 25
                                    }
}
