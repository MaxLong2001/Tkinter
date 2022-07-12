function [Similarity,Energy,ExtrNum] = Calculate(y,x,f)
%UNTITLED3 此处显示有关此函数的摘要
%   分别为相似度，能量，变点数量
extrMaxValue=find(diff(sign(diff(y)))==-2)+1;
ExtrNum=length(extrMaxValue);
[ACF,lags,bounds]=autocorr(y,size(x,2)-1);
plot(lags/f,ACF);
extrMaxValue2=ACF(find(diff(sign(diff(ACF)))==-2)+1);
Energy=sum(abs(y).^2);
Similarity=extrMaxValue2(1);
end

