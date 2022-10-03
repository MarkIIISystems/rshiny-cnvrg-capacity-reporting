library(shiny)
library(ggplot2) 

PV_Capacity_Details <- read.csv("reports/pvCapReport.csv", stringsAsFactors = FALSE)

ui <- fluidPage(
  title = "PV Capacity Report",
  sidebarLayout(
    sidebarPanel(
      conditionalPanel(
        'input.dataset01 === "PV_Capacity_Details"',
        checkboxGroupInput("show_vars", "Columns in PV_Capacity_Details to show:",
                           names(PV_Capacity_Details), selected = names(PV_Capacity_Details))
      )
    ),
    mainPanel(
      tabsetPanel(
        id = 'dataset01',
        tabPanel("PV_Capacity_Details", DT::dataTableOutput("mytable01"))
      )
    )
  )
)

server <- function(input, output) {  

  # choose columns to display
  output$mytable01 <- DT::renderDataTable({
    DT::datatable(PV_Capacity_Details[, input$show_vars, drop = FALSE], options = list(lengthMenu = c(10, 25, 50, 100), pageLength = 50))
  })
}

shinyApp(ui, server)
