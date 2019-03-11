三元组比softmax的优势在于 
softmax不直接，（三元组直接优化距离），因而性能也不好。
softmax产生的特征表示向量都很大，一般超过1000维。
FaceNet并没有像DeepFace和DeepID那样需要对齐。
FaceNet得到最终表示后不用像DeepID那样需要再训练模型进行分类，直接计算距离就好了，简单而有效。
论文并未探讨二元对的有效性，直接使用的三元对。
triplet的特征并不比softmax少，在特征这层上两者是一样的。
但是像google这样用8M个身份的人脸，如果还用softmax的话，最后需要做一个D*8M大小的矩阵乘法，其中D为特征维数。这个的代价就太大了，因此才要使用triplet来避开这个问题。
还有一个优点，triplet不需要每个类有很多样本，现实中很实用。