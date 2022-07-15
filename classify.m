function pre = classify(Q,X,frequency)
pre = [];
%Q是训练模型所用的数据
%X是做分类预测数据的特征值
%frequency是分类次数
%pre用于储存每次分类的结果
for i=1:frequency
   [final_features, final_mark] = sp_IPF_SMOTE(Q(:,1:7),Q(:,8),8);
   md3=fitctree(final_features,final_mark);
   pre = [pre,predict(md3,X)];
end