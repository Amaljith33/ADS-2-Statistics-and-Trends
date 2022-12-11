import matplotlib.pyplot as plt
import pandas as pd


def read(file_name):
    """
    This function is for reading the excel dataset returning both the
    data frame and its transpose.

    Returns
    -------
    Dataframes(original and transpose)
    """
    data = pd.read_excel(file_name)
    data = data.drop(['Series Name', 'Series Code',
                     'Country Code'], axis=1).dropna()
    data_transpose = data.transpose()
    return data, data_transpose


def bar_plot(df_name, title, fig_name, y_label):
    """
    This function is for plotting the bar graph using the datas from the
    returned dataframe.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(17, 18))
    Years = ["1990 [YR1990]", "1995 [YR1995]", "2000 [YR2000]",
             "2005 [YR2005]", "2010 [YR2010]", "2015 [YR2015]"]
    df_name.plot(x="Country Name", y=Years, kind='bar')
    plt.title(title, fontsize=12)
    plt.xlabel('Countries', fontsize=5)
    plt.xticks(fontsize=5, rotation=90)
    plt.ylabel(y_label, fontsize=5)
    plt.yticks(fontsize=5)
    plt.legend(frameon=False, fontsize=6)
    plt.savefig(fig_name, bbox_inches="tight", dpi=200)
    plt.show()


def line_plot(df_name, title, fig_name, y_label):
    """
    This function is for plotting the line graph using the datas from the 
    returned dataframe.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(17, 18))
    Years = ["1994 [YR1994]", "1998 [YR1998]", "2002 [YR2002]",
             "2006 [YR2006]", "2010 [YR2010]", "2014 [YR2014]"]
    df_name.plot(x="Country Name", y=Years, kind='line')
    plt.title(title, fontsize=12)
    plt.xlabel('Countries', fontsize=5)
    plt.xticks(range(0, len(df_name.index)),
               df_name["Country Name"], rotation=90)
    plt.ylabel(y_label, fontsize=5)
    plt.yticks(fontsize=5)
    plt.legend(frameon=False, fontsize=6)
    plt.savefig(fig_name, bbox_inches="tight", dpi=200)
    plt.show()


# Reading the excel file to get a return of dataframes.
REO, REOT = read(
    "Renewable Electricity Output.xlsx")
REC, RECT = read(
    "Renewable Energy Consumption.xlsx")
ANOE, ANOET = read(
    "Agricultural Nitrous Oxide Emissions.xlsx")
CY, CYT = read("Cereal Yield.xlsx")

# Calling the function for plotting the bar graph and the parameters are
# dataframe, title, fig name and the y label.
bar_plot(REO, "Renewable electricity output",
         "REO Bargraph.png", "% of total electricity output")
bar_plot(REC, "Renewable energy consumption",
         "REC Bargraph.png", "% of total final energy consumption")

# Calling the function for plotting the line graph and the parameters are
# dataframe, title, fig name and the y label.
line_plot(ANOE, "Agricultural nitrous oxide emissions",
          "ANOE Linegraph.png", "thousand metric tons of CO2 equivalent")
line_plot(CY, "Cereal_yield (kg per hectare)",
              "CY Linegraph.png", "kg per hectare")
