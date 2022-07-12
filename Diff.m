function [Len] = Diff(a)
%UNTITLED 此处显示有关此函数的摘要
%   此处显示详细说明
extrMaxValue=find(diff(sign(diff(a)))==-2)+1;
Len=length(extrMaxValue);
end

