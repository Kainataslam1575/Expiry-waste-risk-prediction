# Expiry / Waste Risk Prediction

## Project Overview

This project uses Machine Learning to predict whether perishable FMCG
products are at risk of expiring before being sold.

## Problem

Perishable FMCG products such as milk, yogurt, bread and juices have
limited shelf lives. Products may expire before being sold, causing
inventory waste and financial loss.

## Proposed Solution

A Machine Learning classification model predicts expiry/waste risk
using inventory, sales and expiry-related features.

## Input Features

- Current Stock Quantity
- Daily Sales Velocity
- Historical Demand
- Remaining Shelf Life
- Days Until Expiry
- Product Age
- Demand Variability
- Promotion Status
- Previous Sales Trend

## ML Task

Classification

1 = High expiry/waste risk
0 = Low expiry/waste risk

## Algorithm

Decision Tree Classifier

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## Business Solution

High Risk → Promotion / Discount / Transfer

Medium Risk → Monitor / Consider Promotion

Low Risk → Normal Inventory Management

## Business Benefits

- Reduce expired products
- Reduce inventory waste
- Reduce financial loss
- Improve inventory turnover
- Improve inventory management

## Deployment

A web-based dashboard can show:

SKU → Stock → Days to Expiry → Risk → Recommended Action
