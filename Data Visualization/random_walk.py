{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled8.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMOXuFN9m9XZj2z6IKqEbR3",
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
        "<a href=\"https://colab.research.google.com/github/Sn-one/Python-Crash-Course-Sol/blob/main/Untitled8.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZneAXA9elNxt"
      },
      "source": [
        "from random import choice\n",
        "\n",
        "class RandomWalk:\n",
        "  \"\"\" A class to generate Random Walks \"\"\"\n",
        "\n",
        "  def __init__(self, num_points=5000):\n",
        "    \"\"\" Initailize attributes of a Walk \"\"\"\n",
        "    self.num_points = num_points\n",
        "\n",
        "    \"\"\" All walks start at (0,0)\"\"\"\n",
        "\n",
        "    self.x_values = [0]\n",
        "    self.y_values = [0]\n",
        "\n",
        "\n",
        "  def fill_walk(self):\n",
        "    \"\"\" Calculate all points in the walk. \"\"\"\n",
        "    #keep taking steps until the walk reaches a desirable length\n",
        "    while len(self.x_values) < self.num_points:\n",
        "\n",
        "      #decide which direction to go and how far to go in that direction\n",
        "      #x_direction and x_distance\n",
        "      x_direction = choice([1,-1])\n",
        "      x_distance = choice([0,1,2,3,4])\n",
        "      x_step = x_direction * x_distance\n",
        "\n",
        "      #y_direction and y_distance\n",
        "      y_direction = choice([1,-1])\n",
        "      y_distance = choice([0,1,2,3,4])\n",
        "      y_step = y_direction * y_distance\n",
        "\n",
        "      #Reject moves that go nowhere\n",
        "      if x_step ==0  and y_step ==0 :\n",
        "        continue\n",
        "      \n",
        "      #calculate new position \n",
        "      x = self.x_values[-1] + x_step\n",
        "      y = self.y_values[-1] + y_step\n",
        "\n",
        "      self.x_values.append(x)\n",
        "      self.y_values.append(y)\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
