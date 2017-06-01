## Note

*   数据预处理

    *   大学名字匹配。

        因为两个来源的数据中大学名字常不匹配（例如University of California-Berkeley和University of California--Berkeley，或者University of Alabama和The University of Alabama），所以要进行基于经验的消歧。对于一些无法确定的学校，整个tuple被删去。最后一共有210个学校。

        保存在1-new_rank.npy和1-new_stat.npy。

    *   属性选择。

        如果某个属性在这210个学校当中，有不少于150个都是数（而不是字符串或者NULL），那么就把这个属性保留下来。一共1743个属性，由此选出499个属性。这样做，一方面是为了避开全都是字符串或者NULL的无用属性，另一方面是为了不让少量的缺失浪费整个有用属性。缺失的数据由全局平均值补齐。

        保存在2-attr.npy和2-final_stat.npy中。