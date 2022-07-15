function pre = classify(Q,X,frequency)
pre = [];
%Q是训练模型所用的数据
%X是做分类预测数据的特征值
%frequency是分类次数
%pre用于储存每次分类的结果
unhealth_index=find(Q(:,8)==1);%健康数据索引
health_index=find(Q(:,8)==0);%损伤数据索引
rand('seed',1);%设置随机数种子
unhealth_index=unhealth_index(randperm(length(unhealth_index)),:);%打乱损伤数据索引
health_index=health_index(randperm(length(health_index)),:);%打乱健康数据索引
train_index=[health_index(1:613,:);unhealth_index(1:57,:)];%拼接670个训练数据
train_data=Q(train_index,:);%训练数据
for i=1:frequency
   [final_features, final_mark] = sp_IPF_SMOTE(train_data(:,1:7),train_data(:,8),8);
   md3=fitctree(final_features,final_mark);
   pre = [pre,predict(md3,X)];
end