function [final_features, final_mark] = sp_IPF_SMOTE(original_features,original_mark,K)

[final_features ,final_mark] = sp_SMOTE_III(original_features, original_mark,K);%使用SMOTE算法进行加点
ind_n = find(final_mark == 0);%negative位置(0位置)（列向量）
size_n = size(ind_n,1);
size_n9  = ceil(size_n/9);%原多数集个数/9取整
ind_p = find(final_mark == 1);
size_p = size(ind_p,1);
size_p9 = ceil(size_p/9);%原少数集个数/9取整
% inc_node = 20;
test_patterns = final_features;
prediction = zeros(9,size_p+size_n);%9行全集个数列

for i = 1:15
    r = randi([1,size_n],size_n9,1);%在区间[1,size_n]中生成size_n9 * 1的随机整数矩阵 
    r_tr_n = setdiff(ind_n,r);%ind_n中存在但r不存在的数据（从小到大）
    r = randi([size_n+1,size_n+size_p]',size_p9,1);%在区间[size_n+1,size_n+size_p]中生成size_n9 * 1的随机整数矩阵
    r_tr_p = setdiff(ind_p,r);%ind_p中存在但r不存在的数据（从小到大）
    train_patterns = [final_features(r_tr_n,:);final_features(r_tr_p,:)];
    train_targets = [final_mark(r_tr_n,:);final_mark(r_tr_p,:)];
    md3=fitctree(train_patterns, train_targets);%二叉决策树算法
    prediction(i,:) = predict(md3,test_patterns);%生成15行*(size_n+size_p)列测试mark
%     prediction(i,:) = C4_5(train_patterns', train_targets', test_patterns', inc_node);

end
dd = [];
prediction = prediction';%测试集转置，15列*（size_n+size_p）行测试mark
for i = 1:size_p
    nn = size(find(prediction(i,:)==1),2);
    if nn >=8
        dd = [dd;i];
    end
end
for i = size_p+1:size_p+size_n
    %display(prediction(i,:));
    nn = size(find(prediction(i,:)==0),2);
    if nn >=8
        dd = [dd;i];
    end
end
final_features(dd,:) = []; 
final_mark(dd,:) = []; 
%figure;
%gscatter(final_features(:,1),final_features(:,2),final_mark)
%xlabel('Correlation Coefficient');
%ylabel('Normalized Energy');
%legend('healthy & 1-10mm','20mm+')
%legend('healthy & 1-10mm','10-20mm & 20mm+')
