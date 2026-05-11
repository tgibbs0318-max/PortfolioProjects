{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c131715d",
   "metadata": {},
   "source": [
    "# BMI Calculator\n",
    "\n",
    "https://www.cdc.gov/bmi/adult-calculator/index.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ab169ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "#BMI = (weight in pounds x 703) / (height in inches x height in inches)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ed4712f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter you name:  Tina\n",
      "Enter your weight in pounds:  150\n",
      "Enter your height in inches:  62\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "27.43236212278876\n",
      "Tina, you are overweight. You need to exercise more and stop sitting and writing so many python examples referencing ice cream.\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter you name: \")\n",
    "\n",
    "weight = int(input(\"Enter your weight in pounds: \"))\n",
    "\n",
    "height = int(input(\"Enter your height in inches: \"))\n",
    "\n",
    "BMI = (weight * 703) / (height * height)\n",
    "\n",
    "print(BMI)\n",
    "\n",
    "if BMI>0:\n",
    "    if(BMI<18.5):\n",
    "        print(name +\", you are underwight.\")\n",
    "    elif (BMI<=24.9):\n",
    "        print(name +\", you are normal weight.\")\n",
    "    elif (BMI<29.9):\n",
    "        print(name +\", you are overweight. You need to exercise more and stop sitting and writing so many python examples referencing ice cream.\")\n",
    "    elif (BMI<34.9):\n",
    "        print(name +\", you are obese.\")\n",
    "    elif (BMI<39.9):\n",
    "        print(name +\", you are severely obese.\")\n",
    "    else:\n",
    "        print(name +\", you are morbidly obese.\")\n",
    "else:\n",
    "    print(\"Enter valid input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66be944f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "521c5bb8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf0ae710",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2026624b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15b3560f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "103deb3d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d72530fb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a07ad247",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25a3ec13",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10ec78fe",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cd4c947",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17550312",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea0f4997",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76574c3f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
