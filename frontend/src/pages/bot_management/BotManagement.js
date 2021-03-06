import React from "react";
import useStyles from "../livemarkets/styles";
import {
  Grid,
} from "@material-ui/core";
// components
import PageTitle from "../../components/PageTitle/PageTitle";
import AgentList from "./AgentList.js";
import Widget from "../../components/Widget/Widget";

// Charts
import Performance from "./bot_performance.js";
import Assets from "./bot_assets.js";
import Equity from "./Equity.js";
// data
const agent_data= [
    {
      id: 0,
      name: "Auto ITM Closure Agent",
      starttime: "02 July 2020",
      status: "Running",
      equity: [10,11,12,23,23,123,344],
      balances: [{'coin': 'USDT', 'free': 0.0, 'total': 0.0, 'usdValue': 2.5031455e-09},
                 {'coin': 'BTC',
                  'free': 0.08552497,
                  'total': 0.11043491,
                  'usdValue': 1302.8794711600162},
                 {'coin': 'BEAR', 'free': 0.0, 'total': 0.0, 'usdValue': 0.0},
                 {'coin': 'PAXG', 'free': 0.0, 'total': 0.0, 'usdValue': 0.0},
                 {'coin': 'USD',
                  'free': 7.68805447,
                  'total': 7.68805447,
                  'usdValue': 7.688054475573361},
                 {'coin': 'ETH', 'free': 0.0, 'total': 0.0, 'usdValue': 0.0}]

    },
    {
      id: 1,
      name: "Bullish Bot",
      starttime: "05 July 2020",
      status: "Paused"
    },
    {
      id: 2,
      name: "Bearish Bot",
      starttime: "05 June 2020",
      status: "Running"
    },
  ]



export default function BotManagement() {
  var classes = useStyles();
  return (
    <>
      <PageTitle title="Agent Management" />
      <Grid container spacing={4}>
        <Grid item xs={12}>
          <Widget title="Agent Equity" upperTitle noBodyPadding>
            <Equity></Equity>
          </Widget>
        </Grid>
      </Grid>


      { false &&
        <Grid container spacing={4}>
          <Grid item xs={12}>
            <Assets data={agent_data}/> 
          </Grid>
          <Grid item xs={6}>
            <Widget title="Equity by Agent" upperTitle noBodyPadding>
              <Performance />
            </Widget>
          </Grid>
        </Grid>
      }

      <Grid container spacing={4} >
        <Grid item xs={12}>
          <Widget
            title="Currently running Agents"
            upperTitle
            bodyClass={classes.fullHeightBody}
            className={classes.card}>
                <div>
                  <AgentList/>
                </div>
          </Widget>
        </Grid>
      </Grid>
    </>
  );
}
