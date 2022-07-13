
function [final_features ,final_mark] = sp_SMOTE_III(original_features, original_mark,KNN)
%figure;
%gscatter(original_features(:,1),original_features(:,2),original_mark)
%xlabel('Normalized energy');
%ylabel('Normalized Amplitude');
%legend('healthy','damage')
ind = find(original_mark == 1);%����������λ��
P = original_features(ind,:);%����������ֵ
ind1 = find(original_mark == 0);
Q = original_features(ind1,:);
% KNN = 6;
final_features = original_features;
% Limit = size(original_features,1);

Num_Ov = ceil(max(size(find(original_mark == 0),1) - size(find(original_mark == 1),1),size(find(original_mark == 1),1) - size(find(original_mark == 0),1)));%��������������Ĳ�
j2 = 1;
snewall=[];
while j2 <= Num_Ov
    %find nearest K samples from S2(i,:)
    S2= datasample(P,1);%��P�н������ó����������ȡһ�����зŻأ�
%     Condidates = nearestneighbour(S2', P', 'NumberOfNeighbours', min(KNN,Limit));
    Condidates = knnsearch(P, S2,  'k', KNN);%��P���ҵ���S2�������KNN���㣬������λ�ø�ֵ��Condidates
    Condidates(:,1) = [] ;%ȥ����һ�У���Ϊ����ĵ㼴��P����
    Condidates=Condidates';
    h(:,1:7)=datasample(P(Condidates,:),2,'replace',false);
    %h(:,1:3)=datasample(P(Condidates,:),2,'replace',false);
    a=rand(1,3);
    b=sum(a);
    c=a/b;
    snew = c(1).*S2(1,:) + c(2).*h(1,:)+c(3).*h(2,:);%snew=�������ֵ+alpha�����һ����ֵ-�������ֵ��
    final_features = [final_features;snew];%����������������ȫֵ���������������㣩
    snewall=[snewall;snew];
    j2=j2+1;
end
    
mark = 2 * ones(Num_Ov,1);%onesȫ1��
final_mark = [original_mark; mark];%����������������ȫmark���������������㣩
%figure;
%gscatter(final_features(:,1),final_features(:,2),final_mark)
%xlabel('Correlation Coefficient');
%ylabel('Normalized Energy');
%legend('healthy & 1-10mm','20mm+','new points')
%legend('healthy & 1-10mm','10-20mm & 20mm+','new points');
ind2 = find(final_mark == 2);
final_mark(ind2,:)=final_mark(ind2,:)-1;



