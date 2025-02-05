## Introduction/Background

> Provide an introduction of your topic and literature review of related work. Briefly explain your dataset and its features, and provide a link to the dataset if possible. 

[ ] Literature Review 

Deforestation is a persistent issue that has been heavily impacting numerous regions across the world, even those that are not heavily forrested. In a 2009 study by van der Werf et al., deforestation has been identified to be one of the biggest contributors to climate change, producing between 6 and 17 percent of global greenhouse gas emissions[[1]](https://doi.org/10.1038/ngeo671). Due to its effect on exacerbating climate change, it is imperative for deforestation to be mitigated as much as possible. Most countries in possession of vast forested lands such as Brazil have already imposed policies to try to mitigate deforestation and enhance their forest preservation efforts [2](https://www.gov.br/planalto/en/latest-news/2023/06/brazil-announces-measures-to-expand-protection-of-the-amazon). However, an issue with deforestation is that it is often costly for countries to enforce their policies, whether due to the economic incentives that deforestation brings to their often impoverished locals, or because certain drivers of deforestation has not yet been identified.  

In recent years, there have been efforts to use traditional statistical techniques and Machine Learning for automated identification of deforestation using satellite images [3](https://doi.org/10.3390/app13031772). As innovation in the field of Machine Learning continues, researchers have discovered increasingly advanced techniques to estimate various forest biophysical properties [4](https://doi.org/10.1109/JSTARS.2017.2748341), plant pattern identification and classification [5](https://doi.org/10.1109/IROS.2018.8593514), and semantic segmentation [6](https://doi.org/10.1109/LRA.2019.2963823).

For this project, we found the dataset that we will be using through a competition called "Identifying Deforestation Drivers" hosted by Solafune [7](https://solafune.com/competitions/68ad4759-4686-4bb3-94b8-7063f755b43d?menu=about&tab=&ref=mlcontests). The dataset obtained was specifically the **Sentinel-2 Multi-Spectral Instrument, Level 2-A** which is a set of dataset images that resulted from the Sentinel-2 mission by the Copernicus programme sponsored by the European Union Space Agency [8](https://sentiwiki.copernicus.eu/web/s2-applications). By using this dataset, we guarantee that we are working with a common dataset that other researchers may have used in their prior work to evaluate our method against others in a way that is as fair as possible. 

The Sentinel-2 Multi-Spectral Instrument, Level-2A image contains information on 12 bands and includes bands 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B9', 'B11', and 'B12' [7](https://solafune.com/competitions/68ad4759-4686-4bb3-94b8-7063f755b43d?menu=about&tab=&ref=mlcontests). The images have all been processed to mask clouds for Sentinel-2 images from 01/01/2017 to 06/01/2024, and the median of within 2 years of all images is used as the image for that location. All images have been filtered so that only those with more than 95% free of No Data are selected. Additionally, annotations have been provided in the form of JSON documents, where each image has been tagged with a list of identified deforestation drivers as well as polygon information that marks the area where the deforestation driver is identified within this image. 


- Min Lu
- Jaegeon Lee

## Problem Definition

> Identify a problem and motivate the need for a solution. 

[ ] Problem 
[ ] Motivation 

- Aaron

## Methods

> Present proposed solutions including specific data processing methods and machine learning algorithms, and elaborate on why you think each will be effective. It is recommended to identify specific functions/classes in existing packages and libraries (i.e. scikit-learn) rather than coding the algorithms from scratch.

[ ] 3+ Data Preprocessing Methods Identified 
[ ] 3+ ML Algorithms/Models Identified 
[ ] CS 7641: Unsupervised and Supervised Learning Methods Identified 

- Mikhail

## Potential Results and Discussion

Identify several quantitative metrics you plan to use for the project (i.e. ML Metrics). Present goals in terms of these metrics, and state any expected results. 

[ ] 3+ Quantitative Metrics 
[ ] Project Goals (recommended to include sustainability and ethical considerations) 
[ ] Expected Results 

- Naveen

## References

Cite relevant papers and articles utilizing the IEEE format. All reference in this section must have a matching in-text citation in the body of your proposal text. 

1. van der Werf, G. R., Morton, D. C., DeFries, R. S., Olivier, J. G., Kasibhatla, P. S., Jackson, R. B., Collatz, G. J., & Randerson, J. T. (2009). CO2 emissions from Forest loss. Nature Geoscience, 2(11), 737–738.
2. Presidência da República. (2023, June 6). Brazil announces measures to expand protection of the Amazon. Planalto. https://www.gov.br/planalto/en/latest-news/2023/06/brazil-announces-measures-to-expand-protection-of-the-amazon 
3. Sboui, T., Saidi, S., & Lakti, A. (2023). A Machine-Learning-Based Approach to Predict Deforestation Related to Oil Palm: Conceptual Framework and Experimental Evaluation. Applied Sciences, 13(3), 1772.
4. Shao, Z., Zhang, L., & Wang, L. (2017). Stacked sparse autoencoder modeling using the synergy of airborne LiDAR and satellite optical and SAR data to map forest above-ground biomass. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 10(12), 5569-5582.
5. Carpentier, M., Giguere, P., & Gaudreault, J. (2018, October). Tree species identification from bark images using convolutional neural networks. In 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 1075-1081). IEEE.
6. Chen, S. W., Nardari, G. V., Lee, E. S., Qu, C., Liu, X., Romero, R. A. F., & Kumar, V. (2020). Sloam: Semantic lidar odometry and mapping for forest inventory. IEEE Robotics and Automation Letters, 5(2), 612-619.
7. Identifying deforestation drivers - solafune. Solafune. (n.d.). https://solafune.com/competitions/68ad4759-4686-4bb3-94b8-7063f755b43d?menu=about&tab=&ref=mlcontests 
8. S2 applications. SentiWiki. (n.d.). https://sentiwiki.copernicus.eu/web/s2-applications
