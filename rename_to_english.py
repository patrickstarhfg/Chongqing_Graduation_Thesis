import os
import shutil
import subprocess

# Define the mapping of Chinese names to English names
mapping = {
    "上市公司基本信息(年)141052855": "ListedCompanyInfo",
    "上市公司数字化转型指标(年)140715925": "DigitalTransformationIndex",
    "上市公司数字化转型程度(年)140823112": "DigitalTransformationDegree",
    "上市公司股东情况文件143410884": "ShareholderInfo",
    "中国上市公司股权性质文件144138690": "EquityNature",
    "分城市国内生产总值163043201": "CityGDP",
    "分省份国内生产总值162918113": "ProvincialGDP",
    "利润表132634691": "IncomeStatement",
    "数字经济相关产业政策141435335": "DigitalEconomyPolicy",
    "治理综合信息文件142300719": "GovernanceInfo",
    "现金流量表(直接法)133134963": "CashFlowStatement",
    "相对价值指标142624897": "RelativeValueIndex",
    "管理层治理能力152948875": "ManagementGovernanceAbility",
    "资产负债表110235546": "BalanceSheet",
    "“一带一路”政策对企业融资约束的影响研究.pdf": "Research_Belt_and_Road_Financing.pdf",
    "企业全要素生产率（TFP）相关指标.pdf": "TFP_Related_Indicators.pdf",
    "企业数字化转型成熟度测度及影响因素研究_.pdf": "Digital_Transformation_Maturity_Research.pdf",
    "我国碳排放权交易机制的企业减排效应评估_.pdf": "Carbon_Emission_Trading_Mechanism_Evaluation.pdf",
    "数据要素赋能制造业全要素生产率机制研究_.pdf": "Data_Factor_TFP_Mechanism_Research.pdf",
    "绿色创新对企业环境绩效的影响研究——基于.pdf": "Green_Innovation_Environmental_Performance.pdf",
    "论文大纲.md": "Thesis_Outline.md",
    "变量用途说明.md": "Variable_Usage_Description.md",
    "数据获取与处理指南.md": "Data_Acquisition_Guide.md",
    "CSMAR数据下载指南.md": "CSMAR_Download_Guide.md",
    "CSMAR数据下载指南_表2变量.md": "CSMAR_Download_Guide_Table2.md",
    "Git多地协作指南.md": "Git_Collaboration_Guide.md",
    "Git推送指南.md": "Git_Push_Guide.md"
}

def git_mv(src, dst):
    if os.path.exists(src):
        print(f"Renaming '{src}' to '{dst}'...")
        # Use subprocess to call git mv
        try:
            subprocess.run(["git", "mv", src, dst], check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error renaming {src}: {e}")
            # Fallback to os.rename if git mv fails (e.g. not tracked yet)
            # but usually we want git mv.
    else:
        print(f"Source '{src}' not found, skipping.")

if __name__ == "__main__":
    # Ensure we are in the right directory
    target_dir = r"D:\SHLT\cqgs\cqbylw"
    os.chdir(target_dir)
    
    for src, dst in mapping.items():
        git_mv(src, dst)
