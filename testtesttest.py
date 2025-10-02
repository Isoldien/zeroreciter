{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOdfute0UFSRwQjws4tDe3y",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Isoldien/zeroreciter/blob/main/testtesttest.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from datetime import date, timedelta\n",
        "\n",
        "today = date.today()\n",
        "\n",
        "# Dictionary (key and pair) based on Salah + Rakat ----------------------------\n",
        "prayers_dict = {\n",
        "      \"fajr\": 2,\n",
        "      \"dhuhr\": 4,\n",
        "      \"asr\": 4,\n",
        "      \"maghrib\": 3,\n",
        "      \"isha\": 4\n",
        "  }\n",
        "# ----------------------------------------------------------------------------\n",
        "\n",
        "# ----------------------------------------------------------------------------\n",
        "madhab_tuples = [\"hanafi\", \"shafi\", \"maliki\", \"hanbali\"]\n",
        "# ----------------------------------------------------------------------------\n",
        "\n",
        "# Infinite Loop -----------------------------------------------------------------------------------------------------------------\n",
        "while True:\n",
        "  user_factor = int(input('Enter how many sets you wish to do (0 to exit): \\n')) # Ask for user input\n",
        "\n",
        "  total_rakats = sum(prayers_dict.values()) * user_factor # take sum of rakats, mulitplied by user factor (sets)\n",
        "\n",
        "  total_minutes = user_factor * 15 # baseline time, could be changed later. user_factor * 15 to find minutes\n",
        "\n",
        "  total_hours = total_minutes / 60 # convert minutes to hours\n",
        "\n",
        "  print('This is your total rakats: ', total_rakats)\n",
        "\n",
        "  if total_hours < 1 :\n",
        "      print(\"This is how many minutes it would take: \", total_minutes, \"minutes\") # if hours is less than 1, then print minutes\n",
        "  else :\n",
        "      print(\"This is how many hours it would take: \", total_hours, \"hours\") # else print hours\n",
        "\n",
        "# -------------------------------------------------------------------------------------------------------------------------------\n",
        "\n",
        "# Test Qadha calculation --------------------------\n",
        "  user_factor = user_factor * 5\n",
        "\n",
        "  qadha = 11950 / user_factor\n",
        "\n",
        "  print(\"This is how many days your Qadha will take: \", round(qadha, 0))\n",
        "\n",
        "  completion_date = today + timedelta(days=round(qadha, 0))\n",
        "\n",
        "  print(\"This is your completion date: \", completion_date.strftime(\"%d / %m / %y\"))\n",
        "# -------------------------------------------------\n",
        "\n",
        "## Break the Program --------------------------\n",
        "  if user_factor == 0:\n",
        "    break # break the loop --------------------\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 285
        },
        "id": "ORe4r7F-ST9W",
        "outputId": "98fff2d9-bc39-4844-c41a-5dc574cf08ff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter how many sets you wish to do (0 to exit): \n",
            "0\n",
            "This is your total rakats:  0\n",
            "This is how many minutes it would take:  0 minutes\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "ZeroDivisionError",
          "evalue": "division by zero",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-2966235741.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     39\u001b[0m   \u001b[0muser_factor\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0muser_factor\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m5\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     40\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 41\u001b[0;31m   \u001b[0mqadha\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m11950\u001b[0m \u001b[0;34m/\u001b[0m \u001b[0muser_factor\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     42\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     43\u001b[0m   \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"This is how many days your Qadha will take: \"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mround\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mqadha\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mZeroDivisionError\u001b[0m: division by zero"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "from datetime import date, timedelta\n",
        "\n",
        "today = date.today()\n",
        "\n",
        "# Dictionary (key and pair) based on Salah + Rakat ----------------------------\n",
        "prayers_dict = {\n",
        "      \"fajr\": 2,\n",
        "      \"dhuhr\": 4,\n",
        "      \"asr\": 4,\n",
        "      \"maghrib\": 3,\n",
        "      \"isha\": 4\n",
        "  }\n",
        "# ----------------------------------------------------------------------------\n",
        "\n",
        "# ----------------------------------------------------------------------------\n",
        "madhab_tuples = [\"hanafi\", \"shafi\", \"maliki\", \"hanbali\"]\n",
        "# ----------------------------------------------------------------------------\n",
        "\n",
        "# Infinite Loop -----------------------------------------------------------------------------------------------------------------\n",
        "while True:\n",
        "  user_factor = int(input('Enter how many sets you wish to do (0 to exit): \\n')) # Ask for user input\n",
        "\n",
        "  total_rakats = sum(prayers_dict.values()) * user_factor # take sum of rakats, mulitplied by user factor (sets)\n",
        "\n",
        "  total_minutes = user_factor * 15 # baseline time, could be changed later. user_factor * 15 to find minutes\n",
        "\n",
        "  total_hours = total_minutes / 60 # convert minutes to hours\n",
        "\n",
        "  print('This is your total rakats: ', total_rakats)\n",
        "\n",
        "  if total_hours < 1 :\n",
        "      print(\"This is how many minutes it would take: \", total_minutes, \"minutes\") # if hours is less than 1, then print minutes\n",
        "  else :\n",
        "      print(\"This is how many hours it would take: \", total_hours, \"hours\") # else print hours\n",
        "\n",
        "# -------------------------------------------------------------------------------------------------------------------------------\n",
        "\n",
        "# Test Qadha calculation --------------------------\n",
        "  user_factor = user_factor * 5\n",
        "\n",
        "  qadha = 11950 / user_factor\n",
        "\n",
        "  print(\"This is how many days your Qadha will take: \", round(qadha, 0))\n",
        "\n",
        "  completion_date = today + timedelta(days=round(qadha, 0))\n",
        "\n",
        "  print(\"This is your completion date: \", completion_date.strftime(\"%d / %m / %y\"))\n",
        "# -------------------------------------------------\n",
        "\n",
        "## Break the Program --------------------------\n",
        "  if user_factor == 0:\n",
        "    break # break the loop --------------------\n",
        "\n",
        "\"\"\"\n",
        "\n",
        "\"\"\"\n",
        "Qadha Version 0.2\n",
        "\n",
        "- Add functions:\n",
        "  - calculate_total_rakats\n",
        "  - calculate_total_time\n",
        "  - calculate_qadha_days\n",
        "  - calulate_completion_date\n",
        "  - get_user_input\n",
        "  - main_program_loop\n",
        "\n",
        "\"\"\"\n",
        "\n",
        "from datetime import date, timedelta\n",
        "\n",
        "def get_today_date() :\n",
        "  today = date.today()\n",
        "  return today\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "print(get_today_date())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WbEQTPq7LX9Q",
        "outputId": "862d8914-01e5-4922-ec3b-5db370de86af"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2025-10-02\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e9cd80f4"
      },
      "source": [
        "*   `calculate_total_rakats`\n",
        "*   `calculate_total_time`\n",
        "*   `calculate_qadha_days`\n",
        "*   `calculate_completion_date`\n",
        "*   `get_user_input`\n",
        "*   `main_program_loop`"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Misc\n"
      ],
      "metadata": {
        "id": "RXrY9lBNJaoe"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Learnt how timedelta works, including how to add days to a year and the datetime module"
      ],
      "metadata": {
        "id": "3SkhNQATsa6d"
      }
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3f26114d"
      },
      "source": [
        "from datetime import date, timedelta\n",
        "\n",
        "# Get today's date\n",
        "today = date.today()\n",
        "\n",
        "# Example number of days (replace with your variable)\n",
        "number_of_days = 597\n",
        "\n",
        "# Calculate the future date\n",
        "future_date = today + timedelta(days=5000)\n",
        "\n",
        "# Print the result\n",
        "print(f\"Today's date is: {today}\")\n",
        "print(f\"{number_of_days} days from today will be: {future_date}\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Potential function names for programs"
      ],
      "metadata": {
        "id": "zqeHG64_FuKf"
      }
    }
  ]
}