function [final_features, final_mark] = sp_IPF_SMOTE(original_features,original_mark,K)

[final_features ,final_mark] = sp_SMOTE_III(original_features, original_mark,K);%ʹ��SMOTE�㷨���мӵ�
ind_n = find(final_mark == 0);%negativeλ��(0λ��)����������
size_n = size(ind_n,1);
size_n9  = ceil(size_n/9);%ԭ����������/9ȡ��
ind_p = find(final_mark == 1);
size_p = size(ind_p,1);
size_p9 = ceil(size_p/9);%ԭ����������/9ȡ��
% inc_node = 20;
test_patterns = final_features;
prediction = zeros(9,size_p+size_n);%9��ȫ��������

for i = 1:15
    r = randi([1,size_n],size_n9,1);%������[1,size_n]������size_n9 * 1������������� 
    r_tr_n = setdiff(ind_n,r);%ind_n�д��ڵ�r�����ڵ����ݣ���С����
    r = randi([size_n+1,size_n+size_p]',size_p9,1);%������[size_n+1,size_n+size_p]������size_n9 * 1�������������
    r_tr_p = setdiff(ind_p,r);%ind_p�д��ڵ�r�����ڵ����ݣ���С����
    train_patterns = [final_features(r_tr_n,:);final_features(r_tr_p,:)];
    train_targets = [final_mark(r_tr_n,:);final_mark(r_tr_p,:)];
    md3=fitctree(train_patterns, train_targets);%����������㷨
    prediction(i,:) = predict(md3,test_patterns);%����15��*(size_n+size_p)�в���mark
%     prediction(i,:) = C4_5(train_patterns', train_targets', test_patterns', inc_node);

end
dd = [];
prediction = prediction';%���Լ�ת�ã�15��*��size_n+size_p���в���mark
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
